//
//  Section.h
//  Qcumber
//
//  Created by Chris Cooper on 12-01-01.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class SectionComponent;

@interface Section : NSManagedObject

@property (nonatomic, strong) NSNumber * id;
@property (nonatomic, strong) NSNumber * index;
@property (nonatomic, strong) NSManagedObject *course;
@property (nonatomic, strong) NSManagedObject *type;
@property (nonatomic, strong) NSManagedObject *term;
@property (nonatomic, strong) NSSet *components;
@end

@interface Section (CoreDataGeneratedAccessors)

- (void)addComponentsObject:(SectionComponent *)value;
- (void)removeComponentsObject:(SectionComponent *)value;
- (void)addComponents:(NSSet *)values;
- (void)removeComponents:(NSSet *)values;

@end
